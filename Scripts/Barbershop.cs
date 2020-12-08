using System;
using Enums;
using UnityEngine;
using UnityEngine.UI;


[RequireComponent(typeof(BarbersGeneration))]
public class Barbershop : MonoBehaviour
{
    public Text barbersText;
    public Text hourText;
    public Text dayText;

    public int maxHour = 8;

    private int _hour;
    private int _day;
    
    private GameObject[] _barbers;
    private GameObject[] _customers;
    private GameObject[] _regularCustomers;

    private void Start()
    {
        _barbers = gameObject.GetComponent<BarbersGeneration>().Barbers;
        _customers = gameObject.GetComponent<CustomersGeneration>().Customers;
        _regularCustomers = gameObject.GetComponent<CustomersGeneration>().RegularCustomers;
    }

    private void GenerateHour()
    {
        AddTime();
    }

    private void DistributeBarbers()
    {
        for (int i = 0; i < _barbers.Length; i++)
        {
            var barber = _barbers[i].GetComponent<Barber>();
            if (barber.State == StateEn.OnWork)
            {
                Haircut haircut = null;
                foreach (var cust in _customers)
                {
                    var customer = cust.GetComponent<Customer>();
                    haircut = customer.ChoiceHaircut();
                    if (customer.IsWaiting && haircut.Level == barber.Level && maxHour - _hour >= haircut.Time)
                        haircut = haircut;
                    else
                        break;
                }
                barber.Working();
                barber.AddHours(haircut.Time);
                barber.AddCash(haircut.Cost);
            }
        }

        ViewBarbers();
    }

    private void RecountBarbersHours()
    {
        for (int i = 0; i < _barbers.Length; i++)
        {
            var barber = _barbers[i].GetComponent<Barber>();
            if (barber.State != StateEn.Resting)
            {
                if (barber.HoursToEnd() == 0)
                {
                    barber.Resting();
                }
            }
        }
    }

    public void ViewBarbers()
    {
        barbersText.text = "";
        for (int i = 0; i < _barbers.Length; i++)
        {
            var barber = _barbers[i].GetComponent<Barber>();
            barbersText.text += "Level: "+ barber.Level + " Cash: " + barber.Cash + "\n";
        }
    }

    private void AddTime(int hours=1, int days=0)
    {
        AddDay(days);
        _hour += hours;
        if (_hour >= maxHour)
        {
            _hour %= maxHour;
            hourText.text = "Hour:" + _hour + "/" + maxHour;
            AddDay();
        }
    }

    private void AddDay(int amount=1)
    {
        _day += amount;
        dayText.text = "Day:" + _day;
    }
}
