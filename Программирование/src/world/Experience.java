package world;

import java.util.Objects;

public class Experience extends Requirement {
    private int level;
    private String description;
    private int failedAttempts;

    public Experience(int level, String description) {
        this.level = level;
        this.description = description;
        this.failedAttempts = 0;
    }

    public void incrementFailedAttempts() {
        this.failedAttempts++;
        System.out.println("Было много неудачных опытов. Текущие неудачные попытки: " + this.failedAttempts);
    }

    public void gainExperience(int points) {
        this.level += points;
        System.out.println("Получено опыта: " + points + ". Текущий уровень опыта: " + this.level);
    }

    @Override
    public String toString() {
        return "Уровень опыта " + level;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Experience that = (Experience) o;
        return level == that.level;
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(level);
    }

    public int getLevel() {
        return level;
    }

}

