package products;

import java.util.Objects;

public class Milk extends Product implements Perishable {
    private String type;
    private double weight;

    public Milk(String type, double weight) {
        super("молоко");
        this.type = type;
        this.weight = weight;
    }

    @Override
    public String goBad() {
        return getName() + " испортилось";
    }

    @Override
    public String toString() {
        return "Mолоко " + type + " " + weight;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Milk milk = (Milk) o;
        return Double.compare(weight, milk.weight) == 0 && Objects.equals(type, milk.type);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), type, weight);
    }

    @Override
    public double getWeight() {
        return weight;
    }
}


