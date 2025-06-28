package animals;

import java.util.Objects;

public class Goat extends Animal implements Mammals {
    public final static String ANIMAL_NAME = "Коза";
    private int age;
    private Gender gender;
    private ReasonToKill reasonToKill;


    public Goat(int age, Gender gender, ReasonToKill reasonToKill) {
        this.age = age;
        this.gender = gender;
        this.reasonToKill = reasonToKill;
    }

    @Override
    public void giveMilk() {
        if (age > 11 && gender == Gender.FEMALE) {
            System.out.println("Коза производит молоко");
        } else {
            System.out.println("Коза моленькая еще");
        }
    }

    @Override
    public String toString() {
        return "Коза с возрастом " + age;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Goat goat = (Goat) o;
        return age == goat.age && gender == goat.gender;
    }

    @Override
    public int hashCode() {
        return Objects.hash(age, gender);
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Gender getGender() {
        return gender;
    }

    public void setGender(Gender gender) {
        this.gender = gender;
    }

    public ReasonToKill getReasonToKill() {
        return reasonToKill;
    }

    public void setReasonToKill(ReasonToKill reasonToKill) {
        this.reasonToKill = reasonToKill;
    }
}


