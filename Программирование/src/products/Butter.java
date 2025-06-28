package products;

import java.util.Objects;

public class Butter extends Product implements Perishable{
    private String type;
    private double weight;

    public Butter(String type, double weight) {
        super("масло");
        this.type = type;
        this.weight = weight;
    }

    @Override
    public String goBad() {
        return getName()+" испортилось";
    }

    @Override
    public String toString() {
        return "Масло " +type + " " +weight;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Butter butter = (Butter) o;
        return Double.compare(weight, butter.weight) == 0 && Objects.equals(type, butter.type);
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