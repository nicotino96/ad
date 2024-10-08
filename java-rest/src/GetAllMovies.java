import org.json.JSONArray;
import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

import java.util.ArrayList;
import java.util.Comparator;

public class GetAllMovies extends ServerResource {

    @Get
    public StringRepresentation getEndpointResponse() {
        boolean shouldOrderByDurationDesc = false;
        String queryParamValue = getQueryValue("orderByDurationDesc");
        if (queryParamValue != null){
            shouldOrderByDurationDesc = Boolean.parseBoolean(queryParamValue);
        }
        MoviesConnector connector = new MoviesConnector();
        JSONArray resultArray = new JSONArray();
        ArrayList<Movie> databaseFilms = connector.getAll();
        if (shouldOrderByDurationDesc) {
            databaseFilms.sort((m1, m2) -> Integer.compare(m2.getDuration(), m1.getDuration()));
        }
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
