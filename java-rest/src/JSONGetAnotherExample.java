import org.json.JSONObject;
import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

public class JSONGetAnotherExample extends ServerResource {
    @Get
    public StringRepresentation getEndpointResponse() {
        JSONObject json = new JSONObject();
        json.put("characterPopularity", 3);
        json.put("characterDescription","Lisa Simpson es la saxofonista que adora el Jazz y a los animales");
        String jsonString = json.toString();
        StringRepresentation representation = new StringRepresentation(jsonString);
        representation.setMediaType(MediaType.APPLICATION_JSON);
        return representation;
    }
}