import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ResourceException;
import org.restlet.resource.ServerResource;

public class GetMovieByID extends ServerResource {
    @Get
    public StringRepresentation getEndpointResponse() {
        String movieID = getAttribute("movieID");
        Integer movieInt = Integer.parseInt(movieID);
        MoviesConnector connector = new MoviesConnector();

        Movie movie = connector.retrieveMovieUsingID(movieInt);
        if (movie == null) {
            throw new ResourceException(404, "The film was not found");
        }

        // Aquí podríamos controlar que el valor no sea nulo
        // De momento, lo dejamos así
        connector.closeConnection();
        String jsonString = movie.toJSONObject().toString();
        StringRepresentation representation = new StringRepresentation(jsonString);
        representation.setMediaType(MediaType.APPLICATION_JSON);
        return representation;
    }


}
