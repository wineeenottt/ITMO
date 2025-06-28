package time;

import java.util.Objects;

public class Year {
   private double count;
   private String name;

   public Year(String name, double count){
      this.name=name;
      this.count=count;
   }

   @Override
   public String toString() {
      return name +" "+ count;
   }

   @Override
   public boolean equals(Object o) {
      if (this == o) return true;
      if (o == null || getClass() != o.getClass()) return false;
      Year year = (Year) o;
      return Objects.equals(name, year.name);
   }

   @Override
   public int hashCode() {
      return Objects.hashCode(name);
   }

   public double getCount() {
      return count;
   }

   public void setCount(double count) {
      this.count = count;
   }

   public String getName() {
      return name;
   }

   public void setName(String name) {
      this.name = name;
   }
}


