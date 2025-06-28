package building;

public class MilkFarm extends Farm {
    public MilkFarm(String name) {
        super(name);
    }

    @Override
    public void produceProducts() {
        System.out.println("Производится молоко. Получается до двух галлонов молока в день");
    }
}