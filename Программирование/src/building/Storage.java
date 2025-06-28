package building;

import building.exceptions.CheckedException;
import building.exceptions.UncheckedException;
import products.Weighable;

import java.util.ArrayList;
import java.util.List;

public class Storage<T extends Weighable> {
    private final double MAX_WEIGHT = 150;
    private List<T> storage;

    public Storage() {
        storage = new ArrayList<>();
    }

    public void addProduct(T product) {
        storage.add(product);
    }

    public void showStorage(double weight) throws CheckedException {
        checkStorage();

        double totalWeight = 0;
        for (T product : storage) {
            totalWeight += product.getWeight();
        }

        if (totalWeight > MAX_WEIGHT) {
            throw new CheckedException();
        }

        if (totalWeight > weight) {
            System.out.println("У меня теперь был неистощаемый запас " + storage.size() + " продуктов");
        } else {
            System.out.println("Запас продуктов = " + storage.size() + ". Недостаток.");
        }
    }

    private void checkStorage() {
        if (storage.isEmpty()) {
            throw new UncheckedException();
        }
    }
}