package Move;
import ru.ifmo.se.pokemon.*;

public class DreamEater extends SpecialMove {
    static  Type TYPE = Type.PSYCHIC;
    static  double POWER = 100;
    static  double ACCURACY = 100;

    public DreamEater() {
        super(TYPE, POWER, ACCURACY);
    }
    @Override
    protected String describe() {
        return "Применил Dream Eater";
    }

    @Override
    protected void applyOppDamage(Pokemon def, double damage) {
        // Узнаем статус противника
        Status opp = def.getCondition();
        if (opp.equals(Status.SLEEP)) {
            // Изменяем HP противника
            def.setMod(Stat.HP, (int) Math.round(damage));
        }
    }
    @Override
    protected void applySelfEffects(Pokemon p) {
        // Вычисляем количество здоровья покемона
        int vosHP = (int) (p.getStat(Stat.HP) - p.getHP() / 2);
        // Восстанавливаем здоровье
        p.setMod(Stat.HP, vosHP);
    }
}
