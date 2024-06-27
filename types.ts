// bomb

// agent = {
//     agentName: string
//     teamId: int
// }

// abilities = {

// }

// strat: {
//     mapId: string
//     steps: [StepObject]
// }

// bomb

type Ability = RadialAbility | lineAbility;

type items = {
  id: number;
  type: "bomb" | "weapon";
  attachedTo: Actor;
  position: { x: number; y: number };
};


// drop item
// pickup item
// plant blomb
// defuse bomb
// tap bomb (plant or defuse)


type ItemAction = {
  itemId: number;
  loc: { x: number; y: number };
};


type Actor = {
  id: number;
  type: "agent" | "objective" | "items";
  position: { x: number; y: number };
  abilities: { [key: string]: Ability };
};

// TODO: think about res and how to represent it
type abiltyUsed = {
  name: string;
  duration?: number;
  abilityTargets?: Actor[];
  teamId: number;
  startpoint: { x: number; y: number };
  intermdeiatePoints: { x: number; y: number }[];
  endpoint: { x: number; y: number };
};

type RadialAbility = {
  // smoke, molly, etc
  name: string;
  duration?: number;
  radius: number;
};

type lineAbility = {
  name: string;
  duration?: number;
};

type StepObject = {
  time: number;
  agent: {
    name: string;
    positionChange: {
      dx: number;
      dy: number;
      rotation: number;
    };
    AgentAction: abiltyUsed | ItemAction// | diedOrRevived;
  };
};

const jettInitial = { x: 300, y: 400 };

const step1 = {
  agents: {},
  jett: { dx: 500, dy: 500, abilityUsed: { q: "dash", e: "", c: "", x: "" } },
};
const step2 = {
  jett: { dx: 500, dy: 600 },
  sky: { didDie: true },
};

const step3 = {};

const strat = {
  map: "bind",
  steps: [step1, step2, step3],
};

// sage res
const step7 = { res: [] };




// to think about:
// making noise/walking
// shooting
// pathfinding
// TODO: draw data
// TODO: COMMENT DATA