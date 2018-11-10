class NupebController {
    constructor(){
        this.el = {}

        // ********* blocks, div´s and elements
        this.el.jumbo = document.getElementById('jumbo')
        this.el.logo = document.getElementById('nupeb-logo')
        this.el.aboutNupeb = document.getElementById('about-nupeb')
        this.el.nupebMembers = document.getElementById('nupeb-members')
        this.el.nupebContact = document.getElementById('nupeb-contact')
        this.el.nupebActivities = document.getElementById('nupeb-activities')
        this.el.nupebCine = document.getElementById('nupeb-cinedebate')
        this.el.nupebDocs = document.getElementById('nupeb-documents')
        this.el.nupebEvents = document.getElementById('nupeb-events')
        this.el.nupebThemes = document.getElementById('nupeb-themes')
        this.el.nupebReads = document.getElementById('nupeb-reads')
        this.el.nupebMaterials = document.getElementById('nupeb-materials')
        this.el.nupebResearch = document.getElementById('nupeb-research')  
        /*
         *****************************************************************
         *****************************************************************
         *****************************************************************
         *****************************************************************
        */
        
        
        // ****** buttons and links ********
        this.el.btnObjectives = document.getElementById('btn-span-objectives')
        this.el.btnBack = document.getElementById('btn-back-begin-div')
        this.el.btnMembers = document.getElementById('btn-nupeb-members')
        this.el.btnContact = document.getElementById('btn-contact')
        this.el.btnActivities = document.getElementById('btn-activities')
        this.el.btnCine = document.getElementById('btn-cinedebate')
        this.el.btnDocs = document.getElementById('btn-documents')
        this.el.btnEvents = document.getElementById('btn-events')
        this.el.btnMovies = document.getElementById('btn-movies')
        this.el.btnReads = document.getElementById('btn-reads')
        this.el.btnMaterials = document.getElementById('btn-materials')
        this.el.btnResearch = document.getElementById('btn-research')


        this.initPrototypes()
        this.initEvents()

    }
    initEvents(){
        this.el.btnResearch.addEventListener('click', e => {
            this.el.nupebResearch.show() 
            this.el.btnBack.showGrid()

            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnMaterials.addEventListener('click', e => {
            this.el.nupebMaterials.show()
            this.el.btnBack.showGrid()

            this.el.nupebResearch.hide() 
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()          
        })
        this.el.btnReads.addEventListener('click', e => {
            this.el.nupebReads.show()
            this.el.btnBack.showGrid()

            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()          
        })
        this.el.btnMovies.addEventListener('click', e => {
            this.el.nupebThemes.show()
            this.el.btnBack.showGrid()

            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnEvents.addEventListener('click', e => {
            this.el.nupebEvents.show()
            this.el.btnBack.showGrid()

            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnDocs.addEventListener('click', e => {  
            this.el.nupebDocs.show()
            this.el.btnBack.showGrid()
            
            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnCine.addEventListener('click', e => {
            this.el.nupebCine.show()
            this.el.btnBack.showGrid()
            
            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
        })
        this.el.btnActivities.addEventListener('click', e => {
            this.el.nupebActivities.show()
            this.el.btnBack.showGrid()

            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnContact.addEventListener('click', e => {
            this.el.btnBack.showGrid()
            this.el.nupebContact.show()
            
            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebMembers.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnMembers.addEventListener('click', e => {
            this.el.btnBack.showGrid()
            this.el.nupebMembers.show()

            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.aboutNupeb.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnObjectives.addEventListener('click', e => {
            this.el.aboutNupeb.show()
            this.el.btnBack.showGrid()

            this.el.nupebResearch.hide()
            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.jumbo.hide()
            this.el.logo.hide()
            this.el.nupebCine.hide()
        })
        this.el.btnBack.addEventListener('click', e => {
            this.el.jumbo.show()
            this.el.logo.show()

            this.el.nupebMaterials.hide()
            this.el.nupebReads.hide()
            this.el.nupebThemes.hide()
            this.el.nupebEvents.hide()
            this.el.nupebDocs.hide()
            this.el.nupebActivities.hide()
            this.el.aboutNupeb.hide()
            this.el.btnBack.hide()
            this.el.nupebContact.hide()
            this.el.nupebMembers.hide()
            this.el.nupebCine.hide()

            window.scroll(0,0)
        })
        
        window.addEventListener('onchange', e=> {
            console.log('window event onchange')
            window.scroll(0,0)
        })
    }

    initPrototypes(){
        Element.prototype.hide = function () {
            this.style.display = 'none'
            return this
        }
        Element.prototype.show = function () {
            this.style.display = 'block'
            return this
        }
        Element.prototype.showGrid = function () {
            this.style.display = 'grid'
            return this
        }
        Element.prototype.toggle = function () {
            this.style.display = (this.style.display === 'none') ? 'block' : 'none'
            return this
        }
        Element.prototype.on = function (events, fn) {
            events.split(' ').forEach(event => {
                this.el.addEventListener(event, fn)
                //(exemplo para digitar no console) app.el.btnNewContact.on('click mouseover dblclick', (event) => {console.log('evento do botão newContact >>> ', event.type)})
            })
            return this
        }

    }

}

window.onbeforeunload = function(){ 
  //console.log('onbefore')
  window.scrollTo(0,0);   
 }

window.nupebControl = new NupebController()

