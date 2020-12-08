using UnityEngine;
using Enums;

public class BarbersGeneration : MonoBehaviour
{
    [SerializeField] 
    private int juniors = 2;
    
    [SerializeField] 
    private int middles = 2;
    
    [SerializeField] 
    private int seniors = 2;
    
    [SerializeField] 
    private GameObject barberPrefab;
    
    [SerializeField] 
    private Vector3 generatePosition;
    
    [SerializeField]
    private GameObject[] barbers;

    private Barber _getComponent;

    public BarbersGeneration(int barbersAmount)
    {
        barbers = new GameObject[barbersAmount];
    }

    public GameObject[] Barbers => barbers;

    private void GenerateBarbers()
    {
        barbers = new GameObject[juniors + middles + seniors];
        
        float h = 0;
        for (int i = 0; i < juniors; i++)
        {
            var barber = Instantiate(barberPrefab, generatePosition, Quaternion.identity); 
            barber.transform.localScale = new Vector3(0.5f, 0.5f, 1f);
            barber.GetComponent<Barber>().Level = LevelEn.Junior;
            barber.GetComponent<Barber>().AddDays(1);
            barber.name = barber.name + LevelEn.Junior + (i + 1);
            barbers[i] = barber;
            
            var pos = barber.transform.position; 
            barber.transform.position = new Vector3(pos.x, pos.y + h, pos.z);
            h += 1.25f;
        }
        
        for (int i = 0; i < middles; i++)
        {
            var barber = Instantiate(barberPrefab, generatePosition, Quaternion.identity);
            barber.GetComponent<Barber>().Level = LevelEn.Middle;
            barber.GetComponent<Barber>().AddDays(1);
            barber.name = barber.name + LevelEn.Middle + (i + 1);
            barbers[juniors + i] = barber;
            
            var pos = barber.transform.position; 
            barber.transform.position = new Vector3(pos.x, pos.y + h, pos.z);
            h += 1.5f;
        }
        
        for (int i = 0; i < seniors; i++)
        {
            var barber = Instantiate(barberPrefab, generatePosition, Quaternion.identity); 
            barber.transform.localScale = new Vector3(1.5f, 1.5f, 1f);
            barber.GetComponent<Barber>().Level = LevelEn.Senior;
            barber.GetComponent<Barber>().AddDays(1);
            barber.name = barber.name + LevelEn.Senior + (i + 1);
            barbers[juniors + middles + i] = barber;
            
            var pos = barber.transform.position; 
            barber.transform.position = new Vector3(pos.x + .2f, pos.y + h, pos.z);
            h += 2f;
        }
    }

    private void Start()
    {
        GenerateBarbers();
    }
}
