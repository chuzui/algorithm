/*

 * GameObject.cpp
 *
 *  Created on: 2014Äê5ÔÂ13ÈÕ
 *      Author: Administrator


class SpaceShip;
class SpaceStation;
class Asteroid;
class GameObject {
public:
	virtual void collide(GameObject& otherObject) = 0;
	virtual void collide(SpaceShip& otherObject) = 0;
	virtual void collide(SpaceStation& otherObject) = 0;
	virtual void collide(Asteroid& otherobject) = 0;
};

class SpaceShip: public GameObject {
public:
	virtual void collide(GameObject& otherObject);
	virtual void collide(SpaceShip& otherObject);
	virtual void collide(SpaceStation& otherObject);
	virtual void collide(Asteroid& otherobject);
};

void SpaceShip::collide(GameObject& otherObject)
{
	otherObject.collide(*this);
}
*/
