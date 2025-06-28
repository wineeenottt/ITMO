package world;

import animals.Creature;

public class Nature {
    private String gift = "дарами";

    public void teach(Creature creature) {
        System.out.println("Природа, питающая " + creature + ", сама учит нас, " + getLesson());
    }

    private String getLesson() {
        return "как пользоваться ее " + gift;
    }
}



