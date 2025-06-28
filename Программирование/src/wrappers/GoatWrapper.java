package wrappers;
import animals.Goat;
import java.util.ArrayList;
import java.util.List;

public class GoatWrapper {
    private final int YOUNG_AGE = 11;
    private final List<Goat> goats;

    public GoatWrapper() {
        this.goats = new ArrayList<>();
    }

    public void growAllGoats() {
        for (Goat goat : goats) {
            goat.setAge(goat.getAge() + 1);
        }
    }

    public void addGoat(Goat goat) {
        goats.add(goat);
    }

    public void removeGoat(Goat goat) {
        goats.remove(goat);
    }

    public int isHaveChildren() {
        int count = 0;
        for (Goat goat : goats) {
            if (goat.getAge() < YOUNG_AGE) {
                count++;
            }
        }
        return count;
    }

    public List<Goat> getAllGoats(){
        return goats;
    }

    public int getGoatCount() {
        return goats.size();
    }
}
