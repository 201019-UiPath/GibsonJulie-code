using System;

namespace HerosLib
{
    public class Hero
    {
        public int id;         // value type => System.Int32
        public string name;    // reference type

        //constructor
        public Hero()
        {
            id = 1;
            name = "Bombasto";
        }
    }

}
