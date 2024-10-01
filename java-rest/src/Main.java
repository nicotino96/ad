public class Main {
    public static void main(String[] args) {

        MoviesDataProvider provider = new MoviesDataProvider();
        for (String lineOfMyArray : provider.getTwoColumns()) {
            System.out.println(lineOfMyArray);
        }
        SimpleREST myServer = new SimpleREST();
        myServer.runServer();

    }

}
