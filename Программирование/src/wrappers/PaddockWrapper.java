package wrappers;
import building.Paddock;

public class PaddockWrapper {
    private Paddock paddock;

    public PaddockWrapper(Paddock paddock) {
        this.paddock = paddock;
    }

    public void toBeFormedMessage() {
        paddock.toBeFormed();
    }
}


