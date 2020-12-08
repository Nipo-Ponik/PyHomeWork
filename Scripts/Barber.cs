using UnityEngine;
using Enums;

[RequireComponent(typeof(Rigidbody))]
public class Barber : MonoBehaviour
{
    private LevelEn _level;
    private StateEn _state;
    private int _day = 1;
    
    [SerializeField] 
    private int daysRange = 4;
    
    private int _hoursToEnd;

    [SerializeField] 
    private Vector3 startPosition;
    private Rigidbody _rigidbody;
    
    [SerializeField] 
    private float force = 1f;
    private Material _material;

    public Barber(LevelEn level)
    {
        _level = level;
    }
    
    public Barber(LevelEn level, int day)
    {
        _level = level;
        _day = day;
        _day %= daysRange;
    }
    
    public Barber(LevelEn level, int day, int daysRange)
    {
        _level = level;
        _day = day;
        this.daysRange = daysRange;
        _day %= daysRange;
    }
    
    public LevelEn Level { get; set; }
    public StateEn State => _state;
    public int Cash { get; set; }
    public bool IsWorked { get; set; }

    private void StateCheck()
    {
        _day %= daysRange;
        if (_day == 1)
        {
            if (_state == StateEn.Working)
                _material.color = Color.yellow;
            else
            {
                _material.color = Color.green;
                _state = StateEn.OnWork;
            }
        }
        else if (_state != StateEn.Resting)
            Resting();
    }

    public void Working()
    {
        if (_state == StateEn.OnWork)
        {
            _material.color = Color.yellow;
            _state = StateEn.Working;
        }
    }

    public void Resting()
    {
        _rigidbody.AddForce(Vector3.back * force);
        _material.color = Color.red;
        _state = StateEn.Resting;
    }

    public int HoursToEnd()
    {
        if (_hoursToEnd == 1)
        {
            _hoursToEnd--;
            IsWorked = true;
            return 0;
        }
        if (_hoursToEnd == 0)
        {
            IsWorked = true;
            return 0;
        }
        
        return _hoursToEnd;
    }

    public void AddCash(int amount)
    {
        Cash += amount;
    }

    public void AddHours(int amount)
    {
        _hoursToEnd += amount;
    }
    
    public void AddDays(int amount)
    {
        _day += amount;
        _day %= daysRange;
    }

    public void ToStartPosition(Vector3 position)
    {
        gameObject.transform.position = position;
        _state = StateEn.OnWork;
        _material.color = Color.green;
        IsWorked = false;
    }

    private void Start()
    {
        _rigidbody = GetComponent<Rigidbody>();
        _material = gameObject.GetComponent<MeshRenderer>().material;
        StateCheck();
    }
}
