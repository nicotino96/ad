import org.restlet.data.MediaType;
import org.restlet.representation.StringRepresentation;
import org.restlet.resource.Get;
import org.restlet.resource.ServerResource;

public class JSONGetCompany2 extends ServerResource {
    @Get
    public StringRepresentation getEndpointResponse() {
        GrossProfit profit = new GrossProfit(
                2016,
                5012308,
                "EUR"
        );
        Company company = new Company(
                "HBA",
                "Alice Doe",
                profit
        );
        String jsonString = company.toJSONObject().toString();
        StringRepresentation representation = new StringRepresentation(jsonString);
        representation.setMediaType(MediaType.APPLICATION_JSON);
        return representation;
    }
}
