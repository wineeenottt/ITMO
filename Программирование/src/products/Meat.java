package products;

import java.util.Objects;

public class Meat extends Product implements Perishable{
    private String type;
    private double weight;

    public Meat(String type, double weight) {
        super("мясо");
        this.type = type;
        this.weight = weight;
    }

    @Override
    public String goBad() {
        return getName()+" испортилось";
    }

    @Override
    public String toString() {
        return "Mясо " + type + " " +weight;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Meat meat = (Meat) o;
        return Double.compare(weight, meat.weight) == 0 && Objects.equals(type, meat.type);
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

