package products;

import java.util.Objects;

public abstract class Product implements Weighable {
    private String name;

    public Product(String name) {
        this.name = name;
    }

    public String makeMe(){
        return name+" делают";
    }


    @Override
    public String toString() {
        return "Product " + name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return Objects.equals(name, product.name);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(name);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}
