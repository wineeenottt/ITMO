package Move;

import ru.ifmo.se.pokemon.*;

public class Swagger extends StatusMove {
    static Type TYPE = Type.NORMAL;
    static double POWER = 0;
    static double ACCURACY = 100;

    public Swagger() {
        super(TYPE, POWER, ACCURACY);
    }

    @Override
    protected String describe() {
        return "Применил Swagger";
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        // Повышаем атаку цели на 2 этапа
        p.setMod(Stat.ATTACK, +2);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        // Конфузим противника
        Effect.confuse(p);
    }
}
