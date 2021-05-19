window.navigator.geolocation.getCurrentPosition((position) => {
    lat = position.coords.latitude
    long = position.coords.longitude
    const inputLat = document.querySelector("#lat")
    inputLat.value = lat
    const inputLong = document.querySelector("#long")
    inputLong.value = long
})

