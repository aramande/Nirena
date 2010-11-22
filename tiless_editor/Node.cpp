/*****************************************************************************************
/* Desc: Node class. Each node is a backdrop of the map that contains and IndieLib entity
/* that holds all its attributes
/*
/* gametuto.com - Javier López López (javilop.com)
/*
/*****************************************************************************************
/*
/* Creative Commons - Attribution 3.0 Unported
/* You are free:
/*	to Share — to copy, distribute and transmit the work
/*	to Remix — to adapt the work
/*
/* Under the following conditions:
/* Attribution. You must attribute the work in the manner specified by the author or licensor 
/* (but not in any way that suggests that they endorse you or your use of the work).
/*
/*****************************************************************************************/

// ------ Includes -----

#include "Node.h"

/* 
======================================									
Init
====================================== 
*/
Node::Node (int pX, int pY, int pZ, int pId, int pLayer, IND_Surface *pSurface)
{
	// Get IndieLib instante
	mI = CIndieLib::Instance();

	// Surface id
	mId = pId;

	// First, we have to add the entity to the manager
	mI->Entity2dManager->Add (pLayer, &mEntity);

	mEntity.SetSurface (pSurface); 						// Set the surface into the entity
	mEntity.SetHotSpot (0.5f, 0.5f); 					// Set the hotspot (pivot point) centered
	mEntity.SetPosition ((float) pX, (float) pY, pZ);	// Set the position
	mLayer = pLayer;									// Layer where it is created
		
	// Set a collision bounding rectangle. This is used for checking collisions between the mouse pointer
	// and the entity, in order to interact with it
	mEntity.SetBoundingRectangle ("editor", 0, 0, pSurface->GetWidth(), pSurface->GetHeight());
	mEntity.ShowGridAreas (false);
}


/* 
======================================									
End
====================================== 
*/
Node::~Node() 
{
	mI->Entity2dManager->Delete (&mEntity);
}
