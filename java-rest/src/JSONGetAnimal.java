import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

public class JSONGetAnimal extends ServerResource {
    @Get
    public StringRepresentation getEndpointResponse() {

        AnimalFantastico animalFantastico = new AnimalFantastico(
                "Draco blanco de ojos azules",
                347,
                true,
                new Magic(
                        42,
                        "Escupe fuego por la boca que derrite cualquier metal"
                )
        );
        String jsonString = animalFantastico.toJSONObject().toString();
        StringRepresentation representation = new StringRepresentation(jsonString);
        representation.setMediaType(MediaType.APPLICATION_JSON);
        return representation;
    }
}
