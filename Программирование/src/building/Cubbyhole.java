package building;

import java.util.Objects;

public class Cubbyhole extends Building{
    private int size;
    private static int totalCubbyholes = 0;

    public Cubbyhole(int size) {
        super("Закуток");
        this.size = size;
        totalCubbyholes++;
    }

    @Override
    public String toString() {
        return "Закуток с размером: " + size;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Cubbyhole cubbyhole = (Cubbyhole) o;
        return size == cubbyhole.size;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(size);
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public static int getTotalCubbyholes() {
        return totalCubbyholes;
    }
}
