public class Main {
    public static void main(String[] args) {

        MoviesDataProvider provider = new MoviesDataProvider();
        for (String lineOfMyArray : provider.getTwoColumns()) {
            System.out.println(lineOfMyArray);
        }
        MoviesREST server = new MoviesREST();
        server.runServer();


    }

}
