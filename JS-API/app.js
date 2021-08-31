require('dotenv').config()
const path       = require('path')
const fs         = require('fs')
const { google } = require('googleapis')

const CLIENT_ID     = process.env.CLIENT_ID
const CLIENT_SECRET = process.env.CLIENT_SECRET
const REDIRECT_URI  = process.env.REDIRECT_URI
const REFRESH_TOKEN = process.env.REFRESH_TOKEN

const oauth2Client = new google.auth.OAuth2(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI,
)

oauth2Client.setCredentials({refresh_token: REFRESH_TOKEN})

const drive = google.drive({
    version: 'v3',
    auth: oauth2Client,
})
const filePath = path.join(__dirname, 'wallpaper.jpg')

//--------------------------------------------------------
// Upload function
async function uploadFile() {
    try {
        const response = await drive.files.create({
            requestBody: {
                name: 'wallpaper.jpg',
                mimeType: 'image/jpeg',
            },
            media: {
                mimeType: 'image/jpeg',
                body: fs.createReadStream(filePath)
            }
        })

        console.log(response.data)

    } catch (error) {
        console.log(error.message)
    }
}

// uploadFile()

//--------------------------------------------------------
// Delete file
async function deleteFile() {
    try {
        const response = await drive.files.delete({
            fileId: '1fekmdVyZXTB7iPwKy5zrm9LdtGt4OQlE'
        });
        console.log(response.data, response.status)
    } catch (error) {
        console.log(error.message)
    }
}

deleteFile()

//--------------------------------------------------------
// generate public url
async function generatePublicUrl() {
    try {
        const response = await drive.permissions.create({
            fileId: '1V0aODZaxAnVJ6Ioc7l0DzcapaaETWSGe',
            requestBody: {
                role: 'reader',
                type: 'anyone'
            }
        })
        console.log(response.data, response.status)

        const result = await drive.files.get({
            fileId: '1V0aODZaxAnVJ6Ioc7l0DzcapaaETWSGe',
            fields: 'webViewLink, webContentLink'
        })
        console.log(result.data)
    } catch (error) {
        console.log(error.message)
    }
}

// generatePublicUrl()