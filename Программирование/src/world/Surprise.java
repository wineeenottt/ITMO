package world;

import java.util.Objects;

public class Surprise {
    private boolean pleasant;

    public Surprise(boolean pleasant) {
        this.pleasant = pleasant;
    }

    public String getText() {
        return pleasant ? " это был приятный сюрприз" : "  был неприятный сюрприз";
    }

    @Override
    public String toString() {
        return "Surprise " + pleasant;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Surprise surprise = (Surprise) o;
        return pleasant == surprise.pleasant;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(pleasant);
    }
}
