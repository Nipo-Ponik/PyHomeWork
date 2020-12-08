using System;
using System.Collections;
using System.Collections.Generic;
using Enums;
using UnityEngine;

public class MoveTrigger : MonoBehaviour
{
    [SerializeField] 
    private LevelEn level;

    [SerializeField] 
    private bool isWaiting;
    
    [SerializeField] 
    private bool isWaiting2;
    
    [SerializeField] 
    private bool isRegular;

    [SerializeField] 
    private float force;
    
    private void OnTriggerEnter(Collider other)
    {
        if (other.GetComponent<Barber>() != null)
        {
            if (other.GetComponent<Barber>().Level == level)
            {
                var r = other.gameObject.GetComponent<Rigidbody>();
                r.isKinematic = true;
                r.isKinematic = false;
                other.gameObject.GetComponent<Rigidbody>().AddForce(Vector3.right * force);
            }
        }
        else
        {
            var customer = other.GetComponent<Customer>();
            if (customer.IsWaiting && isWaiting)
            {
                var r = other.gameObject.GetComponent<Rigidbody>();
                r.isKinematic = true;
                r.isKinematic = false;
                other.gameObject.GetComponent<Rigidbody>().AddForce(Vector3.right * force);
                return;
            }
            if (!customer.IsWaiting && isWaiting2)
            {
                var r = other.gameObject.GetComponent<Rigidbody>();
                r.isKinematic = true;
                r.isKinematic = false;
                other.gameObject.GetComponent<Rigidbody>().AddForce(Vector3.left * force);
                return;
            }
            if (!customer.IsWaiting && isRegular && !isWaiting && !isWaiting2)
            {
                var r = other.gameObject.GetComponent<Rigidbody>();
                r.isKinematic = true;
                r.isKinematic = false;
                other.gameObject.GetComponent<Rigidbody>().AddForce(Vector3.right * force);
                return;
            }
            if (!customer.IsWaiting && !isRegular && !isWaiting && !isWaiting2)
            {
                var r = other.gameObject.GetComponent<Rigidbody>();
                r.isKinematic = true;
                r.isKinematic = false;
                other.gameObject.GetComponent<Rigidbody>().AddForce(Vector3.right * force);
                return;
            }
        }
    }
}
