package world;

public class Need extends Requirement{

    public void prosper(Human human) {
        if (human.getCurrentLifeStage() == LifeStage.MATURITY) {
            System.out.println("Ведь нужда приспела");
        } else {
            System.out.println("Человек еще не достиг этого момента");
        }
    }
}
