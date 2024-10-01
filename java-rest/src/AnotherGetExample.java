import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

public class AnotherGetExample extends ServerResource {

    @Get
    public String toString() {
        return "El secreto de la vida es...";
    }
}

