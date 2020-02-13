const router = require("express").Router();
const Users = require("../users/users-model.js");
const restricted = require("../auth/restricted-middleware.js");

/*---------Get user Info---------*/ //Works without middleware
router.get("/:id", restricted, (req, res) => {
    Users.getBy({id: req.params.id})
    .then(user => {
        if (user) {
            res.status(200).json({
                
                user})
        } else {
            res.status(404).json({message: "No user with that ID!"})
        }
    })
    .catch(err => {
        res.status(500).json({message: "Database error", error: err})
    })
})

/*---------Update User Info---------*/ //works without middleware
router.put("/:id", restricted, (req, res) => {
    const changes = req.body;
    const id = req.params;

    Users.update(id, changes)
    .then(user => {
        console.log(user);
        res.status(200).json({message: "Updated user", data: user})
    })
    .catch(err => {
        res.status(500).json({message: "Database error", error: err})
    })
})

/*---------Delete User/Account---------*/
router.delete("/:id", restricted, (req, res) => {
    const id = req.params;

    Users.deleteUser(id)
    .then(user => {
        user ? res.status(200).json({message: "Deleted user"}) : res.status(404).json({message: "User does not exist!"});
    })
    .catch(err => {
        console.log(err);
        res.status(500).json({message: "Database error", error: err})
    })
})


module.exports = router;