using UnityEngine;


public class MoveCamera : MonoBehaviour
{
    [SerializeField] 
    private Vector3 secondPosition;
    
    public void Move()
    {
        gameObject.transform.position = gameObject.transform.position != secondPosition ? secondPosition : 
            new Vector3(0, secondPosition.y, secondPosition.z);
    }
}
