import org.restlet.Component;
import org.restlet.data.Protocol;
import org.restlet.routing.VirtualHost;

public class SimpleREST {
    private Component component;

    public void runServer() {
        try {
            this.component = new Component();
            this.component.getServers().add(Protocol.HTTP, 8125);
            VirtualHost host = this.component.getDefaultHost();
            host.attach("/example", SimpleGetExample.class);
            host.attach("/example", SimpleGetExample.class);
            this.component.start();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
    public void stopServer() throws Exception {
        if (this.component != null) {
            this.component.stop();
        }
    }


}
