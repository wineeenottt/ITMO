package world;

import animals.*;
import building.Farm;
import building.MilkFarm;
import products.Butter;
import products.Cheese;
import products.Product;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Human extends Animal implements Mammals{
    private String name;
    private Gender gender;
    private Herd herd;
    private Surprise surprise;
    private Thought currentThought;
    private Farm farm;
    private LifeStage currentLifeStage;
    private List<Experience> experiences;
    private List<Memory> memories;
    private boolean hasMilkedGoat = false;

    public Human(String name,Gender gender, Surprise surprise) {
        this.name = name;
        this.gender = gender;
        this.surprise = surprise;
        this.currentThought = Thought.NOT_THINKING;
        this.currentLifeStage = LifeStage.CHILDHOOD;
        this.experiences = new ArrayList<>();
        this.memories = new ArrayList<>();
    }

    public String describeSurprise() {
        return "Последнее, собственно говоря, для меня " + surprise.getText();
    }

    public String think() {
        return currentThought.getMessage();
    }

    public void raiseGoats() {
        System.out.println(Thought.BEGINNING.getMessage() + Thought.NOT_THINKING.getMessage());
        this.currentThought = Thought.REALIZATION;
    }

    public void setUpMilkFarm() {
        this.farm = new MilkFarm("Молочная ферма");
        System.out.println("Я устроил молочную ферму");
        farm.produceProducts();
    }

    public void growUp() {
        switch (currentLifeStage) {
            case CHILDHOOD:
                currentLifeStage = LifeStage.MATURITY;
                System.out.println("Я еще никогда в жизни не доил корову, тем более козу");
                break;
            case MATURITY:
                currentLifeStage = LifeStage.OLD;
                System.out.println("Я старый");
                break;
        }
    }

    public void see() {
        Butter butter = new Butter("козье",1.5);
        Cheese cheese = new Cheese("козий",1.5);
        switch (currentLifeStage) {
            case CHILDHOOD:
                System.out.println("В детстве я видел, как " + butter.makeMe() + " и " + cheese.makeMe());
                Memory memory = new Memory("Масло","В детстве я видел масло");
                memories.add(memory);
                break;
            case MATURITY:
                System.out.println("Я взрослый, теперь нужно учиться");
                break;
        }
    }

    public void learnAndPersevere() {
        Experience experience = new Experience(0, "Процесс обучения");
        System.out.println("Начало обучения...");

        for (int i = 0; i < 3; i++) {
            experience.incrementFailedAttempts();
            experiences.add(new Experience(experience.getLevel(), "Неудачная попытка " + (i + 1)));
        }

        experience.gainExperience(5);
        System.out.println("После многих неудачных опытов я научился!");
    }

    public void milkGoats() {
        boolean canMilk = false;

        for (Goat goat : herd.getGoats()) {
            if (goat.getGender() == Gender.FEMALE && goat.getAge() > 5) {
                canMilk = true;
                break;
            }
        }

        if (canMilk) {
            hasMilkedGoat = true;
            System.out.println("Я могу доить козу!");
        } else {
            hasMilkedGoat = false;
            System.out.println("Ни одной подходящей козы для доения нет");
        }
    }

    public void makesCheese() {
        if (hasMilkedGoat) {
            System.out.println("Я могу делать сыр!");
        } else {
            System.out.println("Сначала нужно подоить козу, чтобы сделать сыр");
        }
    }

    public void makesButter() {
        if (hasMilkedGoat) {
            System.out.println("Я могу делать масло!");
        } else {
            System.out.println("Сначала нужно подоить козу, чтобы сделать масло");
        }
    }

    @Override
    public String toString() {
        return "Human "+name;
    }

    @Override
    public void giveMilk() {
       if (gender == Gender.FEMALE){
           System.out.println("Я кормлю детей молоком");
       }else {
           System.out.println("У меня нет молока");
       }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Human human = (Human) o;
        return Objects.equals(name, human.name);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(name);
    }

    public Herd getHerd() {
        return herd;
    }

    public void setHerd(Herd herd) {
        this.herd = herd;
    }

    public Surprise getSurprise() {
        return surprise;
    }

    public void setSurprise(Surprise surprise) {
        this.surprise = surprise;
    }

    public Thought getCurrentThought() {
        return currentThought;
    }

    public void setCurrentThought(Thought currentThought) {
        this.currentThought = currentThought;
    }

    public LifeStage getCurrentLifeStage() {
        return currentLifeStage;
    }

    public void setCurrentLifeStage(LifeStage currentLifeStage) {
        this.currentLifeStage = currentLifeStage;
    }

}

