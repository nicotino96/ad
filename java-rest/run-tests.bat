@ECHO off

REM https://stackoverflow.com/questions/6679907/how-do-setlocal-and-enabledelayedexpansion-work
SetLocal EnableDelayedExpansion
rmdir /s /q generated
mkdir generated
SET test_classnames=
REM https://superuser.com/questions/865084/how-to-get-files-list-in-a-folder-with-batch-file-without-file-extensions
for /F "delims=" %%j in ('dir tests /a /b /-p/o:gen') do (
  SET test_classnames=!test_classnames! %%~nj
)
SET tests_fail=unknown


javac -cp lib\*;tests\*;src\* -d generated tests\T* src\*
java -cp lib\*;generated org.junit.runner.JUnitCore %test_classnames% > tests_output.temp

FOR /F "tokens=1-5 delims=(), " %%i IN (tests_output.temp) DO (
  if [%%i] == [OK] (
    if [%%k] == [tests] (
      REM All OK
      SET tests_fail=0
      SET tests_total=%%j
      goto write_output
    )
  )
  if [%%i] == [Tests] (
    if [%%j] == [run:] (
      if [%%l] == [Failures:] (
        REM Not perfect
        SET tests_fail=%%m
        SET tests_total=%%k
        goto write_output
      )
    )
  )
)

:write_output
git show -s --format=%%H > commit_sha.temp
SET /p sha= < commit_sha.temp
SET /A tests_ok = %tests_total% - %tests_fail%
if [%tests_fail%] == [unknown] (
  echo {"commit_info": "%sha%", "tests_ejecutados": "unknown", "tests_exitosos": "unknown" } > results.json
) else (
  echo {"commit_info": "%sha%", "tests_ejecutados": %tests_total%, "tests_exitosos": %tests_ok% } > results.json
)