using System;
using System.Threading;
using UnityEngine;
using UnityEngine.UI;
using Enums;

public class CustomersGeneration : MonoBehaviour
{
    [SerializeField] 
    private int customersAmount = 5;

    [SerializeField] 
    private int regularCustomersAmount = 3;

    [SerializeField] 
    private GameObject barberPrefab;
    
    [SerializeField] 
    private Vector3 generatePosition;
    
    [SerializeField]
    private GameObject[] customers;
    
    [SerializeField]
    private GameObject[] regularCustomers;

    private Barber _getComponent;

    public CustomersGeneration(int customersAmount, int regularCustomersAmount)
    {
        customers = new GameObject[customersAmount];
        regularCustomers = new GameObject[regularCustomersAmount];
    }

    public GameObject[] Customers => customers;
    public GameObject[] RegularCustomers => regularCustomers;

    private void GenerateBarbers()
    {
        customers = new GameObject[customersAmount];
        regularCustomers = new GameObject[regularCustomersAmount];
        
        float h = 4;
        for (int i = 0; i < customersAmount; i++)
        {
            var customer = Instantiate(barberPrefab, generatePosition, Quaternion.identity);
            var level = (LevelEn) UnityEngine.Random.Range(1, Enum.GetNames(typeof(LevelEn)).Length);
            customer.GetComponent<Customer>().Level = level;
            customer.GetComponent<Customer>().IsWaiting = true;
            customer.name += (i + 1);
            customers[i] = customer;

            var pos = customer.transform.position;
            customer.transform.position = new Vector3(pos.x, pos.y + h, pos.z);
            h += 1f;
        }

        for (int i = 0; i < regularCustomersAmount; i++)
        {
            var customer = Instantiate(barberPrefab, generatePosition, Quaternion.identity);
            var level = (LevelEn) UnityEngine.Random.Range(1, Enum.GetNames(typeof(LevelEn)).Length);
            customer.GetComponent<Customer>().Level = level;
            customer.GetComponent<Customer>().IsRegular = true;
            customer.GetComponent<Customer>().IsWaiting = true;
            customer.name += (i + 1);
            regularCustomers[i] = customer;
            
            var pos = customer.transform.position; 
            customer.transform.position = new Vector3(pos.x, pos.y + h, pos.z);
            h += 1f;
        }
    }

    private void UniteCustomers()
    {
        GameObject[] custs = new GameObject[customersAmount + regularCustomersAmount];
        
        for (int i = 0; i < regularCustomersAmount; i++)
        {
            custs[i] = regularCustomers[i];
        }
        
        for (int i = 0; i < customersAmount; i++)
        {
            custs[regularCustomersAmount + i] = customers[i];
        }

        customers = custs;
    }

    private void Start()
    {
        GenerateBarbers();
        UniteCustomers();
    }
}
