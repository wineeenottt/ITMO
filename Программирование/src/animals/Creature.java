package animals;

import java.util.Objects;

public class Creature extends Animal {
    private String type;

    public Creature(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return type + " тварь";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Creature creature = (Creature) o;
        return Objects.equals(type, creature.type);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(type);
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}

