package animals;

import java.util.Objects;

public class Cow extends Animal implements Mammals {
    public final static String ANIMAL_NAME = "Корова";
    private int age;
    private Gender gender;

    public Cow(int age, Gender gender) {
        this.age = age;
        this.gender = gender;
    }

    @Override
    public void giveMilk() {
        if (age >= 3 && gender == Gender.FEMALE) {
            System.out.println("Корова производит молоко");
        } else {
            System.out.println("Корова еще мала");
        }
    }

    @Override
    public String toString() {
        return "Корова с возрастом " + age;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Cow cow = (Cow) o;
        return age == cow.age;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(age);
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
}

