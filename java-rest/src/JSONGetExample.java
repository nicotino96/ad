import org.json.JSONObject;
import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

public class JSONGetExample extends ServerResource {
    @Get
    public StringRepresentation getEndpointResponse() {
        JSONObject json = new JSONObject();
        json.put("message", "Esto es un JSON de prueba");
        String jsonString = json.toString();
        StringRepresentation representation = new StringRepresentation(jsonString);
        representation.setMediaType(MediaType.APPLICATION_JSON);
        return representation;
    }
}