package building;

public class Gate {
    private Paddock connectedPaddock;

    public Gate(Paddock connectedPaddock) {
        this.connectedPaddock = connectedPaddock;
    }

    public Paddock getConnectedPaddock() {
        return connectedPaddock;
    }

    public void setConnectedPaddock(Paddock connectedPaddock) {
        this.connectedPaddock = connectedPaddock;
    }
}
