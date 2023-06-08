// variables
let title = document.querySelector('#div_id_title')
let image = document.querySelector('#div_id_image')
let ingredientForm = document.querySelectorAll('.ingredient-form')
let addIngredient = document.querySelector('#add-ingredient')
let totalForms = document.querySelector('#id_recipeingredient_set-TOTAL_FORMS')
let ingredientLabel = document.querySelector('#ingredient_label')
let formNum = ingredientForm.length - 1
let line = document.querySelector('#bottom-line')
let formContainer = document.querySelector('#form-container')
let stepForm = document.querySelectorAll('.step-form')
let addStep = document.querySelector('#add-step')
let totalSteps = document.querySelector('#id_recipestep_set-TOTAL_FORMS')
const ingredientSection = document.getElementById('ingredients-section')
const stepSection = document.getElementById('steps-section')
const category = document.getElementById('id_category')
const time = document.getElementById('id_time')
let stepNum = stepForm.length - 1

// base form
title.classList.add('grow')
image.classList.add('grow')
image.querySelector('input').classList.add('w-full')
time.classList.add('py-0.5')

$(function() {
  $(category).select2({
    containerCssClass: 'error'
  })
})

// step
addStep.addEventListener('click', addDetail)

function addDetail(e) {
  e.preventDefault()

  let newForm = stepForm[0].cloneNode(true)
  let formRegex = RegExp(`recipestep_set-(\\d){1}-`, 'g')

  stepNum++
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, `recipestep_set-${stepNum}-`)
  newForm.innerHTML = newForm.innerHTML.replace()
  // formContainer.insertBefore(newForm, ingredientLabel)
  stepSection.insertBefore(newForm, line)
  totalSteps.setAttribute('value', `${stepNum + 1}`)
}

// ingredient
addIngredient.addEventListener('click', addForm)

function addForm(e) {
  e.preventDefault()

  let newForm = ingredientForm[0].cloneNode(true)
  let formRegex = RegExp(`recipeingredient_set-(\\d){1}-`,'g')

  formNum++
  newForm.innerHTML = newForm.innerHTML.replace(formRegex, `recipeingredient_set-${formNum}-`)
  newForm.innerHTML = newForm.innerHTML.replace()
  // ingredientLabel.insertBefore(newForm, line)
  ingredientSection.insertBefore(newForm, line)
  // formContainer.insertBefore(newForm, line)
  totalForms.setAttribute('value', `${formNum + 1}`)

  $(function() {
    $(newForm.querySelector('select')).select2({
      tags: true
    })
  })

  newForm.classList.remove('hidden')
  let options = newForm.querySelector('.select2-container')
  let quantity = newForm.querySelector('.textinput')
  options.style.width = '60%'
  quantity.classList.add('py-0.5')
  quantity.parentNode.classList.add('grow')
}