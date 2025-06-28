package Move;
import ru.ifmo.se.pokemon.*;
public class Facade extends PhysicalMove {
    static  Type TYPE = Type.PSYCHIC;
    static  double POWER = 70;
    static double ACCURACY = 100;

    public Facade() {
        super(TYPE, POWER, ACCURACY);
    }
    @Override
    protected String describe() {
        return "Применил Facade";
    }
    @Override
    protected void applyOppDamage(Pokemon def, double damage) {
        // Получаем статус противника
        Status cond = def.getCondition();
        if (cond.equals(Status.BURN) || cond.equals(Status.POISON) || cond.equals(Status.PARALYZE)) {
            // Применяем урон х2
            def.setMod(Stat.HP, (int) Math.round(damage) * 2);
        }
        else {
            // Применяем обычный урон
            def.setMod(Stat.HP, (int) Math.round(damage));
        }
    }
}

