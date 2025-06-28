package building;
import java.util.ArrayList;
import java.util.List;

public class PaddockNetwork {
    private List<Paddock> paddocks;
    private List<Gate> gates;

    public PaddockNetwork() {
        paddocks = new ArrayList<>();
        gates = new ArrayList<>();
    }

    public void connectPaddocks() {
        for (int i = 0; i < paddocks.size() - 1; i++) {
            Paddock paddock1 = paddocks.get(i);
            Paddock paddock2 = paddocks.get(i + 1);
            Gate gate = new Gate(paddock2);
            paddock1.addGate(gate);
            gates.add(gate);
        }

        System.out.println("Загоны соединены между собой воротами");
    }

    public void addPaddock(Paddock paddock) {
        paddocks.add(paddock);
    }

    public List<Paddock> getPaddocks() {
        return paddocks;
    }
}



