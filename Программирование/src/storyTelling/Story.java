package storyTelling;

import animals.*;
import building.Cubbyhole;
import building.Paddock;
import building.PaddockNetwork;
import building.Storage;
import building.exceptions.CheckedException;
import products.Butter;
import products.Cheese;
import products.Meat;
import products.Milk;
import time.*;
import world.*;
import wrappers.GoatWrapper;
import wrappers.PaddockWrapper;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Story {
    private final int GOAT_COUNT = 12;
    private final int GOAT_AGE_INT = 10;
    private final int GOAT_INCREASE = 31;

    public void run() {
        Year year15 = new Year("года", 1.5);

        System.out.println("Через " + year15);

        GoatWrapper goatWrapper = new GoatWrapper();

        for (int i = 0; i < GOAT_COUNT; i++) {
            goatWrapper.addGoat(new Goat(i + GOAT_AGE_INT, Gender.MALE, ReasonToKill.TO_BUY));
        }

        System.out.println("Было штук " + goatWrapper.getGoatCount() + " " + Goat.ANIMAL_NAME);
        if (goatWrapper.isHaveChildren() == 0) {
            System.out.println("Не считая козлят");
        } else {
            System.out.println("Считая с " + goatWrapper.isHaveChildren() + " козлятами");
        }

        Year year2 = new Year("год", 2);
        System.out.println("А еще через " + year2);
        Surprise surprise = new Surprise(true);
        Human human = new Human("Fermer", Gender.FEMALE, surprise);
        Herd herd = new Herd();
        herd.setGoats(goatWrapper.getAllGoats());
        human.setHerd(herd);

        if (human.getHerd().equals(herd)) {
            System.out.println("Мое");
        } else {
            System.out.println("Не мое");
        }

        List<Goat> newGoats = new ArrayList<>();
        for (int i = 0; i < GOAT_INCREASE; i++) {
            newGoats.add(new Goat(i + GOAT_AGE_INT, Gender.FEMALE, ReasonToKill.TO_BUY));
        }
        Goat goatToEat = new Goat(30, Gender.FEMALE, ReasonToKill.TO_EAT);
        newGoats.add(goatToEat);

        herd.increase(newGoats);

        Time time1 = new Time();
        System.out.println(time1 + " у меня");

        Random random = new Random();
        PaddockNetwork paddockNetwork = new PaddockNetwork();
        int[] cubbyholeSizes = {15, 10, 6};
        for (int i = 1; i <= 5; i++) {
            Paddock paddock = new Paddock("Загон " + i);
            int randomSize = cubbyholeSizes[random.nextInt(cubbyholeSizes.length)];
            Cubbyhole cubbyhole = new Cubbyhole(randomSize);
            paddock.addCubbyhole(cubbyhole);

            PaddockWrapper wrapper = new PaddockWrapper(paddock);
            wrapper.toBeFormedMessage();
            paddockNetwork.addPaddock(paddock);
        }

        System.out.println("Общее количество закутков: " + Cubbyhole.getTotalCubbyholes());
        System.out.println("Общее количество загонов: " + Paddock.getTotalCount());
        paddockNetwork.connectPaddocks();
        for (Paddock paddock : paddockNetwork.getPaddocks()) {
            for (Goat goat : herd.getGoats()) {
                paddock.addGoat(goat);
            }
        }
        System.out.println("Все козы загнаны в закутки");
        Storage<Milk> milkStorage = new Storage<>();
        Storage<Meat> meatStorage = new Storage<>();

        for (int i = 0; i < 100; i++) {
            milkStorage.addProduct(new Milk("Козье молоко", 0.3));
            meatStorage.addProduct(new Meat("Козье мясо", 0.7));
        }

        try {
            milkStorage.showStorage(30);
            meatStorage.showStorage(30);
        } catch (CheckedException e) {
            System.out.println(e.getMessage());
        }

        System.out.println(human.describeSurprise());
        human.raiseGoats();
        System.out.println("Потом " + human.think());

        human.setUpMilkFarm();

        Creature goat = new Creature("всякую");
        Nature nature = new Nature();
        nature.teach(goat);
        human.see();
        human.growUp();
        human.see();
        Need need = new Need();
        need.prosper(human);

        human.learnAndPersevere();

        human.milkGoats();
        human.makesCheese();
        human.makesButter();

        Storage<Butter> butterStorage = new Storage<>();
        Storage<Cheese> cheeseStorage = new Storage<>();

        for (int i = 0; i < 100; i++) {
            butterStorage.addProduct(new Butter("козье", 0.3));
            cheeseStorage.addProduct(new Cheese("козий", 0.7));
            milkStorage.addProduct(new Milk("козье", 0.3));
        }

        try {
            butterStorage.showStorage(30);
            cheeseStorage.showStorage(30);
            milkStorage.showStorage(30);
        } catch (CheckedException e) {
            System.out.println(e.getMessage());
        }

    }
}

