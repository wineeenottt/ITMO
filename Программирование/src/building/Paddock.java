package building;

import animals.Goat;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Paddock extends Building {
    private String name;
    private List<Cubbyhole> cubbyholes;
    private List<Gate> gates;
    private List<Goat> goats;
    private static int totalCount = 0;

    public Paddock(String name) {
        super(name);
        this.cubbyholes = new ArrayList<>();
        this.gates = new ArrayList<>();
        this.goats = new ArrayList<>();
        totalCount++;
    }

    public void toBeFormed() {
        System.out.println("Образовался загон! Текущее количество загонов " + totalCount);
        System.out.println("Закуток в загоне устроен!");
        for (Cubbyhole cubbyhole : cubbyholes) {
            System.out.println(cubbyhole);
        }
    }

    public void addCubbyhole(Cubbyhole cubbyhole) {
        cubbyholes.add(cubbyhole);
    }

    public void addGate(Gate gate) {
        this.gates = new ArrayList<>();
        gates.add(gate);
    }

    public void addGoat(Goat goat) {
        goats.add(goat);
    }

    @Override
    public String toString() {
        return "Загон " + name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Paddock paddock = (Paddock) o;
        return Objects.equals(name, paddock.name);
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(name);
    }

    public static int getTotalCount() {
        return totalCount;
    }

    public String getName() {
        return name;
    }
}

