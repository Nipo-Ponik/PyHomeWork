using System;
using Enums;
using UnityEngine;
using Random = UnityEngine.Random;


public class Customer : MonoBehaviour
{
    private bool _isRegular;
    private bool _isWaiting;
    private readonly LevelEn _level;

    public Customer(LevelEn level, bool isRegular)
    {
        _level = level;
        _isRegular = isRegular;
    }

    public LevelEn Level { get; set; }
    public bool IsWaiting { get; set; }
    public bool IsRegular { get; set; }

    public Haircut ChoiceHaircut()    // Generate & choice
    {
        Array values = Enum.GetValues(typeof(HaircutEn));
        int rand = Random.Range(1, values.Length);
        HaircutEn randomHaircut = (HaircutEn)values.GetValue(rand);

        int cost;
        int time;
        if (rand % (values.Length / 3) == 0)
        {
            cost = 100 * (rand - 1) ^ 2; // 100 - start cost 
            time = 1 * (rand - 1) ^ 2;    // 1 hour - start time: junior - 1 hour, middle - 2...
        }
        else
        {
            cost = 100 * rand ^ 2;
            time = 1 * rand ^ 2;  
        }
        
        Haircut haircut = new Haircut(_level, cost, time);
        return haircut;
    }
    
    public void ToStartPosition(Vector3 position)
    {
        gameObject.transform.position = position;
    }
}