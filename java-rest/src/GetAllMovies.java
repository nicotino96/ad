import org.json.JSONArray;
import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

import java.util.ArrayList;

public class GetAllMovies extends ServerResource {

    @Get
    public StringRepresentation getEndpointResponse() {
        MoviesConnector connector = new MoviesConnector();
        JSONArray resultArray = new JSONArray();
        ArrayList<Movie> databaseFilms = connector.getAll();
        for (Movie mov : databaseFilms) {
            resultArray.put(mov.toJSONObject());
        }
        connector.closeConnection(); // No olvidemos cerrar la conexión
        String jsonString = resultArray.toString();
        StringRepresentation representation = new StringRepresentation(jsonString);
        representation.setMediaType(MediaType.APPLICATION_JSON);
        return representation;

    }
}
