using UnityEngine;
using Enums;

public class Haircut : MonoBehaviour
{
    private readonly LevelEn _level;
    private int _cost;
    private int _time;

    public Haircut(LevelEn levelEn, int cost, int time)
    {
        _level = levelEn;
        _cost = cost;
    }

    public LevelEn Level => _level;
    public int Cost => _cost;
    public int Time => _time;
}
