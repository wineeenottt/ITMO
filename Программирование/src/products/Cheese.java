package products;

import java.util.Objects;

public class Cheese extends Product implements Perishable{
   private String type;
   private double weight;

   public Cheese(String type, double weight) {
      super("сыр");
      this.type = type;
      this.weight = weight;
   }

   @Override
   public String goBad() {
      return getName()+" испортилось";
   }

   @Override
   public String toString() {
      return "Cыр " + type + " " +weight;
   }

   @Override
   public boolean equals(Object o) {
      if (this == o) return true;
      if (o == null || getClass() != o.getClass()) return false;
      if (!super.equals(o)) return false;
      Cheese cheese = (Cheese) o;
      return Double.compare(weight, cheese.weight) == 0 && Objects.equals(type, cheese.type);
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


